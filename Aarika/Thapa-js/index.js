// console.log("Hello World")

// var a = 10;
// var b = 4;
// a= a+b;
// b=a-b;
// a=a-b;
// console.log(a);
// console.log(b);

// console.log("Enter a year: ");

// function leapYear(year){
//     if( (0 == year % 4) && (0 != year % 100) || (0 == year % 400) ){
//         console.log(year + 'it is an leap year....');
//     }
//     else
//     {
//         console.log(year + 'it is not a leap year..');
//     }
// }

// const r = year("Enter the year:");
// leapYear(year);
// program to check leap year
// for(var num = 1; num<=10 ;num++ ){
//     console.log("8 * " + num + " = " + 8*num )
// }
// const sum  = () => `The sum of the two number is  ${(a=5)+(b=7)}`;
// console.log(sum()) ;
// var myFr = ["Aaru","Jaini","Monika","alpha","Beta","Gama"]; 
// for(var i = 0; i< myFr.length;i++){
//     console.log(myFr[i]);
// }
// for (let elements in myFr) {
//    console.log(elements);
// }
// for(let elements of myFr ){
//     console.log(elements);
// }
// myFr.forEach(function(element,index,array) {
//     console.log(element);
//     console.log(element + " index of : " + index)
// });

// const months = ['Jan','Feb','March','May','July']
// const newMonth = months.splice(5,0,'sept'); //(kaha pr add krne ha uski index,delete,string )
// console.log(months)
// const array1=[2,9,5,7,9,32,45]
// let newArr = array1.map((curEle,index,array)=>{
//     return `Index no = ${index} and the value ${curEle} of the ${array}`
// });
// console.log(newArr);
// let array = [25,36,49,81,100];
// const newArr = array.map((curEle) => Math.sqrt(curEle));
// console.log(newArr);
// let arr = [5,6,2];
// let sum = arr.reduce((accumulator,curEle,index,arr) => {return accumulator*=curEle; })
// console.log(sum)
// const arr = [
//     [zone_1,zone_2],
//     [zone_3,zone_4],
//     [zone_5,zone_6],
//     [zone_7,zone_8],
// ];
// let flatArr = arr.reduce((accumu,curval)=>{
//     return accumu.concat(curval);
// });
// console.log(flatArr);
// let arr = "Mango,Banana,Chickoo";
// let arr4 = arr.slice(0,-5);
// console.log(arr4);
// challenge: to display only 28 characters
// let myTweets = "WHAT IS NATURE? There is a great deal of talk and endeavour to protect //nature, the animals, the birds, th
// let myActTweets = myTweets.slice(0,286);
// console.log(myActTweets);
// let date = new Date;
// console.log(date);
// console.log(Date.now());  //shows upto time in ms
