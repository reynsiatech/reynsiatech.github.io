print("Welcome to AITS - Mathematics generation code! please answer the following questions.")

# title = str(input("Title of the Chapter: "))
no_of_questions = int(input("No of questions you want to ask: "))

# question_list = []
answer_list = []
# solution_list = []

for i in range(no_of_questions):
    # question_list.append(str(input("Enter image name of " + str(i+1) + " question: ")))
    answer_list.append(str(input("Enter answer (A/B/C/D) of " + str(i+1) + " question: ")))
    # solution_list.append(str(input("Enter image name of " + str(i+1) + " solution: ")))

# file_name = str(input("Enter file name with .html estension: "))
file_name = "AITS-Mathematics.html"


final_html_code = """
<!DOCTYPE html>
<html>
<head>
<title>Unchaai - Chapter Test</title>
<meta content="width=device-width, initial-scale=1.0" name="viewport">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
<style type="text/css">

	@media (max-width: 768px) {
		.title{
			font-size: 25px;
	}
	.responsive-img{
		width: 100%;
		height: 100%;
	}
	.text_have{
		font-size: 25px;
	}
	.text_given{
		font-size: 18px;
	}
	.text_ques{
		font-size: 18px;
	}

    }

	@media (min-width: 1024px) {

	}


</style>
</head>
<body>
<nav>
<div class="nav-wrapper" style="background: linear-gradient(45deg, #1de099, #1dc8cd);">
<a href="#" class="brand-logo">UnchaAI</a>
</div>
</nav>
<div class="row" style="padding: 20px;">
<div class="col s12 m8 l6 offset-m2 offset-l3">
<div class="test_title">
<h3 class="title">
"""


final_html_code += "All India Test Series - Mathematics" #title

final_html_code += """
</h3>
<p><strong>Rule 1</strong>: Please try to do it by your own.</p>
<p><strong>Rule 2</strong>: Be fully prepared before attempting these questions</p>
<p><strong>Rule 3</strong>: Please try to answer the following questions correctly!</p>
</div>
<form id="question_form" style="margin-top: 50px;">
"""


quest_template = """

<div class="question">
<h5 class="text_ques">Question {}</h5>
<img class="responsive-img" src="Q/{}.PNG">
<p>
<label>
<input name="quest{}" value="A" type="radio" />
<span>Option A</span>
</label>
</p>
<p>
<label>
<input name="quest{}" value="B" type="radio" />
<span>Option B</span>
</label>
</p>
<p>
<label>
<input name="quest{}" value="C" type="radio" />
<span>Option C</span>
</label>
</p>
<p>
<label>
<input name="quest{}" value="D" type="radio" />
<span>Option D</span>
</label>
</p>
</div>
</br></br>
"""


for i in range(no_of_questions):
    final_html_code += quest_template.format(i+1, i+1, i+1, i+1, i+1, i+1)


final_html_code += """
</form>
<div id="confirm_submit" class="modal">
<div class="modal-content">
<h5>Are you sure, you want to submit the quiz?</h5>
</div>
<div class="row">
<div class="col s10 offset-s1">
<form>
<input type="text" name="name" placeholder="Enter your name!!" id="name">
<input type="text" name="mobile_no" placeholder="Enter your mobile no!!" id="mobile_no">
</form>
</div>
</div>
<div class="modal-footer">
<button class="modal-close btn waves-effect waves-light blue" style="background: linear-gradient(45deg, #1de099, #1dc8cd);">Cancel</button>
<button class="btn waves-effect waves-light blue" style="background: linear-gradient(45deg, #1de099, #1dc8cd);" onclick="evaluate_quiz()">Submit</button>
</div>
</div>
<div id="submit_button" style="text-align: center; margin-top: 30px; margin-bottom: 40px;">
<button class="btn waves-effect waves-light blue modal-trigger" href="#confirm_submit" style="background: linear-gradient(45deg, #1de099, #1dc8cd);">Submit Quiz</button>
</div>
<div id="quiz_score">
<h3 class="text_have">You have scored</h3>
<h2 class="score"></h2>
<h4 class="text_given">in the given quiz!!!</h4>
<button class="btn waves-effect waves-light" style="background: linear-gradient(45deg, #1de099, #1dc8cd);" onclick="see_solution()">See Solution</button>
</div>
<div id="quiz_solution">
"""

solution_template = """
<h5>Question {}</h5>
<img class="responsive-img" src="Q/{}.PNG">
<h6 style="color: blue; font-weight: bold;">Correct Answer: {}</h6>
<h6 style="color: Red; font-weight: bold;" id="ans_{}">Your Answer: </h6>
<img class="responsive-img" src="A/{}.PNG">
</br></br>
"""

for i in range(no_of_questions):
    final_html_code += solution_template.format(i+1, i+1, answer_list[i], i+1, i+1)


final_html_code += """
</div>
</div>
</div>
<script>
$(document).ready(function(){
$('.modal').modal();
// $('#modal').modal('open');
$("#quiz_score").hide();
$("#quiz_solution").hide();
});
var correect_answers = ['"""

for i in range(no_of_questions-1):
    final_html_code += answer_list[i] + "', '"
final_html_code += answer_list[no_of_questions-1] + "']"


final_html_code += """
function print_score(score) {
$("#question_form").remove();
$("#submit_button").remove();
$("#quiz_score").show();
$(".score").append("<strong>" + score + "%</strong>");
}

function get_results(user_ans) {
var len = correect_answers.length;
var num_correct = 0;
for (var i = 0; i < len; i++) {
if (user_ans[i] == correect_answers[i]) {
num_correct += 1;
}
}
var score = (num_correct/len) * 100;
return score;
}

function append_user_answers(user_answers){
	var n = user_answers.length;
	for (var i = 0; i < n; i++) {
		num = i + 1;
		if (user_answers[i] == "") $("#ans_" + num).append("Blank");
		else $("#ans_" + num).append(user_answers[i]);
	}
}

function evaluate_quiz(){
var name = document.getElementById("name").value;
var mobile_no = document.getElementById("mobile_no").value;
if (name != "" && mobile_no != "") {
$('.modal').modal('close');
var num_quest = $(".question").length;
var user_answers = [];
for (var i = 1; i <= num_quest; i++) {
var ans = $("input[name = 'quest"+i+"']:checked").val();
if (ans) {user_answers.push(ans);}
else {user_answers.push("");}
}

var score = get_results(user_answers);
var perform = user_answers.join();
var answers = correect_answers.join();
append_user_answers(user_answers);
submit_form(name, mobile_no, score, perform, answers);
print_score(score);
}
}

function submit_form(name, mobile_no, score, perform, answers) {
var page_location = window.location.href;
var res = page_location.split("/");
res = res[res.length - 1];
res = res.split(".");
var page_name = res[0];

$.ajax({
url: 'https://script.google.com/macros/s/AKfycby-uchi8wXfa0Y0g0tKY9KeUbpRSMlGLnWgGmeMGwatPhrhqWI/exec',
type: 'POST',
data: {
"Sheet_Type": "AITS-Mathematics",
"Sheet_Name": page_name,
"Name": name,
"Mobile_No": mobile_no,
"Score": score,
"Performance": perform,
"Answers": answers
},
error: function() {
console.log("Your form didn't submitted!!!")
},
success: function(data) {

},
});
}

function see_solution() {
$("#quiz_score").remove()
$("#quiz_solution").show();
}


</script>
</body>
</html>

"""

file = open(file_name, "wt")
file.write(final_html_code)
file.close()
