import { Component, OnInit, ViewChild } from '@angular/core';
import { User } from 'src/app/models/User';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.sass']
})
export class UsersComponent implements OnInit {
  user: User = {
    firstname: "",
    lastname: "",
    email: ""
  };
  users: User[];
  showExtended: boolean = true;
  loaded:boolean = false;
  enableAdd: boolean = false;
  currentClasses = {};
  currentStyles = {};
  showUserForm: boolean = false;
  @ViewChild('userForm') form:any;


  constructor() { }

  //inject construction
  ngOnInit(): void {
    setTimeout(() => {
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
      

    this.loaded = true
    }, 800);
    

    

    this.showExtended = true;
    this.setCurrentClasses();
    this.setCurrentStyles();

  }

  addUser() {
    /* this.users.unshift(this.user)
    this.user.isActive = true
    this.user.registered = new Date;

    this.user = {
      firstname: "",
      lastname: "",
      email: ""
  } */
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

  toggleHide(user:User) {
    //very smart way to toggle a value
    user.hide = !user.hide;
  }

  onSubmit({value, valid}: {value: User, valid: boolean}) {
    if(!valid) {
      console.log("Form is not legit!");
    }
    else {
      value.isActive = true;
      value.registered = new Date();
      value.hide = true;
      this.users.unshift(value)

      this.form.reset();
    }
  }

}
