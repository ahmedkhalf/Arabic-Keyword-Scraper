counter = 1
content = ""

function send_word_input(){
    text = document.getElementById("wordlist").value;
    eel.lookup_words(text);
    reset_meaning()
}

function reset_meaning(){
    document.body.innerHTML = "<div class=\"container\"></div>"
    document.body.firstElementChild.innerHTML += "<h1 class=\"title\">Arabic Keyword Scraper</h1>"
    counter = 1
    content = ""
}

eel.expose(add_meaning);
function add_meaning(text){
    content += "<input type=\"radio\" name=\"gender\" id=\"b" + counter + "\"><label class=\"meaning\" for=\"b" + counter + "\">" + text + "</label><br>";
    counter += 1
}

eel.expose(print_meaning);
function print_meaning(){
    document.body.firstElementChild.innerHTML += content
    document.body.firstElementChild.innerHTML += "<a class=\"button button-primary\">Next</a><br>"
}