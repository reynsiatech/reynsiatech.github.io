print("Welcome to test generation code! please answer the following questions.")

title = str(input("Title of the Quiz: "))
no_of_questions = int(input("No of questions you want to ask: "))

question_list = []
answer_list = []
solution_list = []

for i in range(no_of_questions):
    question_list.append(str(input("Enter image name of " + str(i+1) + " question: ")))
    answer_list.append(str(input("Enter answer (A/B/C/D) of " + str(i+1) + " question: ")))
    solution_list.append(str(input("Enter image name of " + str(i+1) + " solution: ")))

file_name = str(input("Enter file name with .html estension: "))


final_html_code = """
<!DOCTYPE html>
<html>
<head>
<title>Unchaai Quiz - Organic Chemistry</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
</head>
<body>
<nav>
<div class="nav-wrapper" style="background-color: #5E50F9;">
<a href="#" class="brand-logo">unchaAI</a>
</div>
</nav>
<div class="row">
<div class="col s12 m8 l6 offset-m2 offset-l3">
<div class="test_title" style="text-align: center">
<h3>
"""


final_html_code += title

final_html_code += """
</h3>
<p>Please try to answer the following questions correctly!</p>
</div>
<form id="question_form">
"""


quest_template = """
<div class="question">
<h5>Question #{}</h5>
<img class="responsive-img" src="questions/{}">
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
<input name="ques{}" value="C" type="radio"  />
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
"""


for i in range(no_of_questions):
    final_html_code += quest_template.format(i+1, question_list[i], i+1, i+1, i+1, i+1)


final_html_code += """
</form>
<div id="confirm_submit" class="modal">
<div class="modal-content">
<h5>Are you sure, you want to submit the quiz?</h5>
</div>
<div class="modal-footer">
<button class="modal-close btn waves-effect waves-light blue">Cancel</button>
<button class="modal-close btn waves-effect waves-light blue" onclick="evaluate_quiz()">Submit</button>
</div>
</div>
<div id="submit_button" style="text-align: center; margin-top: 30px; margin-bottom: 40px;">
<button class="btn waves-effect waves-light blue modal-trigger" href="#confirm_submit">Submit Quiz</button>
</div>
<div id="quiz_score">
<h3>You have scored</h3>
<h2 class="score"></h2>
<h4>in the given quiz!!!</h4>
<button class="btn waves-effect waves-light" onclick="see_solution()">See Solution</button>
</div>
<div id="quiz_solution">
"""

solution_template = """
<h5>Question #{}</h5>
<img class="responsive-img" src="questions/{}">
<h6>Solution: {}</h6>
<img class="responsive-img" src="solutions/{}">
"""

for i in range(no_of_questions):
    final_html_code += solution_template.format(i+1, question_list[i], answer_list[i], solution_list[i])


final_html_code += """
</div>
</div>
</div>
<script>
$(document).ready(function(){
$('.modal').modal();
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
print_score(score);
}
function evaluate_quiz(){
var num_quest = $(".question").length;
var user_answers = [];
for (var i = 1; i <= num_quest; i++) {
var ans = $("input[name = 'quest"+i+"']:checked").val();
if (ans) {user_answers.push(ans);}
else {user_answers.push("");}
}
get_results(user_answers);
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
