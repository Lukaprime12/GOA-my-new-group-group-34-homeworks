age = 100
Name = "Luka"
if(age < 18) {
    console.log("Access denied ! come when you are 18 MR." , Name)
}
else if(age >= 18) {
    console.log("Access granted ! congratulations MR." , Name)
}

// what is dot notations in JS ? When you create an object , you give that object properties , and you can reach; 
// those properties using dot notation ;
// example:  const myArr{
//                         Name: "Luka";      
//                         Surname: "Mtchedlidze";
//                         Age: 15;
//                         bestAcademy: "Goa";
//                      };
//            console.log(myArr.Name);
// as you can see here we are logging the objects property Name which we can reach by using dot notation;