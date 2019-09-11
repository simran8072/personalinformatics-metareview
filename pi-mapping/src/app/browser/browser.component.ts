import { Component, OnInit } from '@angular/core';
import clusterMap from "../../assets/cluster_map.json";
import renameMap from "../../assets/rename_map.json";
import { PapersService } from '../papers.service';
import { TagsService } from '../tags.service';

@Component({
  selector: 'app-browser',
  templateUrl: './browser.component.html',
  styleUrls: ['./browser.component.css']
})
export class BrowserComponent implements OnInit {
	codes:string[];
	clusters:{} = {};
	checked:{} = {};
	counts:{} = {};
	paperList:string[] = [];
	search:string;
  hidden:{} = {};


  constructor(private papers:PapersService, private tags:TagsService) { }

  ngOnInit() {
  	this.codes = clusterMap.map(c => c['title']);
  	this.codes.forEach(c => {
      let cm = clusterMap.filter(m => c == m['title'])[0];
  		this.clusters[c] = cm['clusters'];
  		this.checked[c] = {};
      this.hidden[c] = true;
  		cm['clusters'].forEach(cm => {
  			let ids = this.tags.getIdsForTag(cm);
  			if(ids) {
  				this.counts[cm] = ids.length;
  			} else {
  				this.counts[cm] = 0;
  			}
  		});
  		this.clusters[c].sort((a, b) => this.counts[b] - this.counts[a]);
  	});
  	this.paperList = this.papers.getAllPapers();
  }

  getName(code:string) {
    if(!(code in renameMap)) {
      if(code.toLowerCase() != code) {
        //There's probably something to preserve in the code's case
        return code;
      } else {
        //Convert it to title case
        return code.toLowerCase().split(' ').map((s) => s.charAt(0).toUpperCase() + s.substring(1)).join(' ');
      }
    } else if(renameMap[code]) {
      return renameMap[code];
    } else {
      return null;
    }
  }

  clear() {
    this.codes.forEach(c => {
      this.checked[c] = {};
    });
    this.search = null;
    this.check();
  }

  toggleHide(code:string) {
    this.hidden[code] = !this.hidden[code];
  }

  checkBoxes():string[] {
  	let papersSoFar = this.papers.getAllPapers();
  	
  	this.codes.forEach(code => {
  		let papersForCode = [];
  		Object.keys(this.checked[code]).forEach(k => {
  			if(this.checked[code][k]) {
  				papersForCode = papersForCode.concat(this.tags.getIdsForTag(k));
  			}
  		});
  		if(papersForCode.length > 0) {
  			papersSoFar = papersSoFar.filter(p => papersForCode.includes(p));
  		}
  	});

  	return papersSoFar;
  }

  check() {
	this.paperList = this.checkBoxes();
  }

  searchFor() {
  	let searchList = this.papers.filterBy(this.search);
  	this.paperList = this.checkBoxes().filter(p => searchList.includes(p));
  }

}
