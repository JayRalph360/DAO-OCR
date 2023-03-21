let stringChecker = (textToCheck) => {
	let pattern = /([a-z]|[A-Z])+/g;
	let result = textToCheck.match(pattern);
	if(result==textToCheck){
		//code to run if it satisfies
		windows.alert("login sucessful")
	}else{
		//display an error
		windows.alert("unknown value for username")
	}
}
stringChecker("username")