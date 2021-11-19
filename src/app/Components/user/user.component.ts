import { Component } from "@angular/core";
import { OnInit } from "@angular/core";

import { User } from "src/app/models/User";
@Component({
    selector: "app-user",
    templateUrl: './user.component.html',
    styleUrls: ['./user.component.sass']
    
})

export class UserComponent implements OnInit{
    //Properties
    user: User;
    

    //Methods
    constructor() {

    }

    ngOnInit() {
        this.user = {
            firstname: 'John',
            lastname: "Doeinson",
            email: "Jhonny@john.com"
        }
    }

}