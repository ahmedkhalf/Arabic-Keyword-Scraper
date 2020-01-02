var words = [];
var meanings = [];
var selected = [];
var pointer = 0;

window.addEventListener("load", function(){
    eel.expose(add_meaning);
    function add_meaning(list){
        meanings = list;
        document.getElementById("loading").style.display = "none";

        var meanings_div = document.getElementById("meanings");
        meanings_div.innerHTML = "<h3>Select prefered meaning for word: " + words[pointer] + "</h3>";
        for (let i = 0; i < meanings.length; i++) {
            var meaning_node = document.createElement('div'); 
            meaning_node.className = "meaning-btn";     
            meaning_node.innerHTML = '<input type="radio" id="b'+i.toString()+'" name="meaning"><label class="meaning" for="b'+i.toString()+'">'+meanings[i].replace(")", ")<br />")+'</label>';
            meanings_div.appendChild(meaning_node);
        }
    }

    eel.request_words()(function(words_list){
        words = words_list;
        if(words.length == 0){
            window.location.pathname = "wordinput.html";
        }
    });
    
    eel.get_meaning(pointer);
});

function reset_meanings(){
    meanings = [];
}

function next_keyword(){
    pointer += 1;
    meanings_radio = document.getElementsByName("meaning");
    var selection = null;
    for(var i = 0; i < meanings_radio.length; i++){
        if(meanings_radio[i].checked){
            selection = meanings_radio[i].id;
            selection = parseInt(selection.substring(1, selection.length));
        }
    }
    if(selection != null){
        selected.push(selection);
        if(pointer >= words.length){
            var meanings_div = document.getElementById("meanings");
            meanings_div.innerHTML = "";
            document.getElementById("final-step").className = "";
            document.getElementById("back-next").className = "hidden";
            eel.generate_doc(selected)(function(value){
                if(value == true){
                    document.getElementById("final-step").className = "hidden";
                    document.getElementById("file-done").className = "";
                }
            });
        }else{
            reset_meanings();
            eel.get_meaning(pointer);
            document.getElementById("loading").style.display = "block";
        }
    }
}

function open_file(mode){
    eel.open_file(mode);
}
