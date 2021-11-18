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
  enableAdd: boolean = true;
  currentClasses = {};
  currentStyles = {};


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
          },
          image: "https://m.media-amazon.com/images/I/41h5C9nRU9L._AC_.jpg",
          balance:100,
          registered: new Date("01/02/2018 08:30:00")
      },
      {
        firstname: 'Fritz',
        lastname: "Doeinson",
        age: 43,
        adress: {
            street:"Schlüterweg 5",
            city: "Bochum",
            state: "Northrhine Westfalia"
        },
        image: "http://lorempixel.com/600/600/people/3",
        isActive:true,
        balance:77,
        registered: new Date("11/07/2015 02:40:00")
    },
    {
      firstname: 'Peter',
      lastname: "Doeinson",
      age: 43,
      adress: {
          street:"Schlüterweg 5",
          city: "Bochum",
          state: "Northrhine Westfalia"
      },
      image: "https://m.media-amazon.com/images/I/91BLCCISDTL._AC_SL1500_.jpg",
      isActive:false,
      balance:504,
      registered: new Date("01/02/2018 08:30:00")
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
          },
          image: "https://www.toygamewiz.com/media/catalog/product/cache/35/image/650x/040ec09b1e35df139433887a97daa66f/t/-/t-remoteblackbb9_2_.jpg"
      }
      );

    this.loaded = true
    }, 800);
    

    

    this.showExtended = true;
    this.setCurrentClasses();
    this.setCurrentStyles();

  }

  addUser(user:User) {
    this.users.push(user)
  }

  setCurrentClasses() {
    this.currentClasses = {
      "btn-success":this.enableAdd,
      "big-text":this.showExtended
    }
  }
  setCurrentStyles() {
    this.currentStyles = {
      'padding-top': this.showExtended ? '0' : '100px',
      'font-size': this.showExtended ? '' : '35px'
    }
  }

}
