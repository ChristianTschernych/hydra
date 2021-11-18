import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/models/User';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.sass']
})
export class UsersComponent implements OnInit {
  users: User[];
  showExtended: boolean = true;
  loaded:boolean = false;


  constructor() { }

  //inject construction
  ngOnInit(): void {
    setTimeout(() => {
      this.users = [
        {
          firstname: 'John',
          lastname: "Doeinson",
          age: 43,
          adress: {
              street:"Schlüterweg 5",
              city: "Bochum",
              state: "Northrhine Westfalia"
          }
      },
      {
        firstname: 'Fritz',
        lastname: "Doeinson",
        age: 43,
        adress: {
            street:"Schlüterweg 5",
            city: "Bochum",
            state: "Northrhine Westfalia"
        }
    },
    {
      firstname: 'Peter',
      lastname: "Doeinson",
      age: 43,
      adress: {
          street:"Schlüterweg 5",
          city: "Bochum",
          state: "Northrhine Westfalia"
      }
  }
      ]
      this.addUser(
        {
          firstname: 'Satan',
          lastname: "hand",
          age: 34,
          adress: {
              street:"saulage 5",
              city: "Essen",
              state: "Northrhine Westfalia"
          }
      }
      );

    this.loaded = true
    }, 2000);
    

    

    this.showExtended = true;

  }

  addUser(user:User) {
    this.users.push(user)
  }

}
