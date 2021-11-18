export interface User {
        firstname:string,
        lastname:string,
        age:number,
        adress?: {
            street:string,
            city:string,
            state:string
        },
        image?:string,
        isActive?:boolean,
        balance?:number,
        registered?:any
}