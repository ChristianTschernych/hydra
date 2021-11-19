export interface User {
        firstname:string,
        lastname:string,
        email: string,
        image?:string,
        isActive?:boolean,
        balance?:number,
        registered?:any,
        hide?: boolean
}