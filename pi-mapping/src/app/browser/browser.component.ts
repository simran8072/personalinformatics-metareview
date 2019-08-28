import { Component, OnInit } from '@angular/core';
import clusterMap from "../../assets/cluster_map.json";
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


  constructor(private papers:PapersService, private tags:TagsService) { }

  ngOnInit() {
  	this.codes = Object.keys(clusterMap);
  	this.codes.forEach(c => {
  		this.clusters[c] = clusterMap[c];
  		this.checked[c] = {};
  		clusterMap[c].forEach(cm => {
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
