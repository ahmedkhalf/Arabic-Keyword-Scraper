function send_word_input(){
    text = document.getElementById("wordlist").value;
    eel.lookup_words(text);
    window.location.pathname = "wordselect.html";
}