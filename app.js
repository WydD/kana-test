var content = null;
var index = -10;
var tries = -1;
var start = null;
var sessionErrors = 0;
var totalCount = 0;
var successCount = 0;
var cumulativeSpeed = 0;
var templateResult = '<tr><td><span class="glyphicon glyphicon-$1" aria-hidden="true"></span></td><td>$2</td><td>$3</td><td>$4</td><td>$5</td></tr>';

function draw() {
    if (content == null || index < 0) {
        return;
    }
    var isKata = $("#type").val() == "kata";
    var txt = content[index];
    $("#label").text(isKata ? wanakana.toKatakana(wanakana.toRomaji(txt)): txt);
    $("#stats").text("Speed: "+(cumulativeSpeed/(Math.max(successCount, 1))).toFixed(2)+" sec/char, Errors: "+sessionErrors);
    $("#test").focus();
}

function next() {
    if (tries == 0) {
        cumulativeSpeed += computeTypeSpeed($("#label").text());
        successCount += 1;
    }
    index = Math.floor(Math.random()*content.length);
    start = new Date().getTime();
    tries = 0;
    totalCount += 1;
    $("#test").val("");
    draw();
}

function computeTypeSpeed(toGuess) {
    return (((new Date().getTime() - start) / 1000) / toGuess.length);
}
function getTemplateResult(result, given, expected) {
    var toGuess = $("#label").text();
    return $(templateResult
        .replace('$1', result ? "ok" : "remove")
        .replace('$2', toGuess)
        .replace('$3', given)
        .replace('$4', expected)
        .replace('$5', computeTypeSpeed(toGuess).toFixed(2) + " sec/char")
    );
}

function answer(result) {
    var romanji = wanakana.toRomaji(content[index]);
    if (result.trim() == romanji) {
        $("#result tbody").prepend(getTemplateResult(true, result, ""));
        next();
    } else {
        if (tries == 0) {
            sessionErrors += 1;
            draw();
        }
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