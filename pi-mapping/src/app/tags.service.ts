import { Injectable } from '@angular/core';
import tags from "../assets/all_tags.json";

@Injectable({
  providedIn: 'root'
})
export class TagsService {

  constructor() { }

  getIdsForTag(tag:string) {
  	if(tag in tags) {
  		return tags[tag];
  	}
  	return null;
  }
}
