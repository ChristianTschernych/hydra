import { Injectable } from '@angular/core';

import { User } from '../models/User';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {

  users: User[];

  constructor() {
    this.users = [
      {
        firstname: 'John',
        lastname: "Doeinson",
        email: "John@gmail.com",
        balance:100,
        registered: new Date("01/02/2018 08:30:00"),
        hide:true
    },
    {
      firstname: 'Fritz',
      lastname: "Doeinson",
      email: "Fritz@gmail.com",
      isActive:true,
      balance:77,
      registered: new Date("11/07/2015 02:40:00"),
      hide:true
  },
  {
    firstname: 'Peter',
    lastname: "Doeinson",
    email: "Peter@gmail.com",
    isActive:false,
    balance:504,
    registered: new Date("01/02/2018 08:30:00"),
    hide:true
}
    ]

   }

   getUsers(): User[] {
     console.log("Fetching users from service:");
     this.users.forEach(element => {
       console.log("Fetched: " + element.firstname + " " + element.lastname)
     });
     return this.users;
   }
}
