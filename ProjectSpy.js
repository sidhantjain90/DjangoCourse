alert("Welcome to the site !");
var FirstName = prompt("Enter your first name");
var LastName = prompt("Enter your last name");
var Age = prompt("Enter your age");
var Height = prompt("Enter your height (in cms)");
var PetName = prompt("Enter your pet name");

if(FirstName[0] === LastName[0] && Age<30 && Age>20 && Height>=170 && PetName[PetName.length -1]==="y"){
  console.log("Welcome comrade !");
}else {
  console.log("There is nothing to see here !");
}
