function checkAnswer(){
	var student_answer= document.getElementById("answer_5").value;
	console.log(student_answer);
	if(student_answer==117){

		document.querySelector("#result").innerHTML = "<h4>Right Answer </h4>";
	}else{
		document.querySelector("#result").innerHTML = "<h4> Try Again </h4>"
	}
}

function checkAnswer1(){
	var student_answer= document.getElementById("answer_6").value;
	console.log(student_answer);
	if(student_answer==56){

		document.querySelector("#result1").innerHTML = "<h4>Right Answer </h4>";
	}else{
		document.querySelector("#result1").innerHTML = "<h4> Try Again </h4>"
	}
}