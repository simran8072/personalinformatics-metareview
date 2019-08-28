import { Component, OnInit, Input } from '@angular/core';
import { PapersService } from '../papers.service';

@Component({
  selector: 'app-paper',
  templateUrl: './paper.component.html',
  styleUrls: ['./paper.component.css']
})
export class PaperComponent implements OnInit {
	@Input() id:string;
  display:boolean = false;
	author:string;
	link:string;
	title:string;
	doi:string;
	keywords:string[];
	tags:string[];
	venue:string;
	year:string;

  constructor(private papers:PapersService) {
  }

  ngOnInit() {
  	let paper = this.papers.getPaper(this.id);
    if(paper) {
      this.display = true;
      this.author = paper.author;
      this.link = paper.link;
      this.title = paper.title;
      this.doi = paper.doi;
      this.keywords = paper.keywords;
      this.tags = paper.tags;
      this.venue = paper.venue;
      this.year = paper.year;
    } else {
      this.display = false;
    }
  }

}
