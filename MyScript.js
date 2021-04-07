function timesFive(numInput){
  var result = numInput*5
  return result
}


// Global Scope
var v= " GLOBAL V"
var stuff = "GLOBAL STUFF"

function fun(stuff){
  console.log(v);
  stuff  = "Reassign stuff inside func"
  console.log(stuff);
}

fun()
console.log(stuff);
