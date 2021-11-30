import { Component, OnInit, ViewChild } from '@angular/core';
import { User } from 'src/app/models/User';
import { MyServiceService } from 'src/app/services/my-service.service';

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


  constructor(private myService:MyServiceService) { }

  //inject construction
  ngOnInit(): void {
    setTimeout(() => {
      
      //fetch all users
      this.users = this.myService.getUsers();

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
