var content = null;
var index = -10;
var tries = 0;
var start = null;

var templateResult = '<tr><td><span class="glyphicon glyphicon-$1" aria-hidden="true"></span></td><td>$2</td><td>$3</td><td>$4</td><td>$5</td></tr>';

function draw() {
    if (content == null || index < 0) {
        return;
    }
    var isKata = $("#type").val() == "kata";
    var txt = content[index];
    $("#label").text(isKata ? wanakana.toKatakana(wanakana.toRomaji(txt)): txt);
    $("#test").focus();
}

function next() {
    index = Math.floor(Math.random()*content.length);
    start = new Date().getTime();
    tries = 0;
    $("#test").val("");
    draw();
}

function getTemplateResult(result, given, expected) {
    return $(templateResult
        .replace('$1', result ? "ok" : "remove")
        .replace('$2', $("#label").text())
        .replace('$3', given)
        .replace('$4', expected)
        .replace('$5', ((new Date().getTime() - start) / 1000)+"s")
    );
}

function answer(result) {
    var romanji = wanakana.toRomaji(content[index]);
    if (result.trim() == romanji) {
        $("#result tbody").prepend(getTemplateResult(true, result, ""));
        next();
    } else {
        tries += 1;
        if (tries == parseInt($("#max-tries").val())) {
            $("#result tbody").prepend(getTemplateResult(false, result, romanji));
            next();
        } else {
            $("#result tbody").prepend(getTemplateResult(false, result, ""));
            start = new Date().getTime();
        }
    }
}

$.ajax("hira.list").done(function(data) {
    content = data.split("\n");
    next();
});