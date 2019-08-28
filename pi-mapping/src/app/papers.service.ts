import { Injectable } from '@angular/core';
import papers from "../assets/all_papers.json";

@Injectable({
  providedIn: 'root'
})
export class PapersService {

  constructor() { 
  }

  getAllPapers() {
  	return Object.keys(papers);
  }

  getPaper(id:string) {
  	if(id in papers) {
  		return papers[id];
  	}
  	return null;
  }

  filterBy(text:string) {
    let paperList = Object.keys(papers);
    let ret = [];
    paperList.forEach(p => {
      let values = Object.values(papers[p]);
      if(values.some(v => (v.toString() as string).toLowerCase().includes(text.toLowerCase()))) {
        ret.push(p);
      }
    });
    return ret;
  }
}
