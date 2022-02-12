"use strict";

function greet() {
    let text = document.getElementById('box').value;
    window.open("https://api.whatsapp.com/send/?phone=%2B91" + text + "&text=Hi+there%2C%0AWe%27re+from+Takshak%2721+organizing+team%2C%0AWe%27re+reaching+out+to+you+since+you%27ve+registered+for+the+event+%22Web+development+with+React%22%0AHere%27s+the+link+to+join+the+WhatsApp+group%0A%0Ahttps%3A%2F%2Fchat.whatsapp.com%2FBdo8hX2uFNGCVN8lBPRQ02&app_absent=0");
    return false;
}
document.getElementById('go').addEventListener('click', greet);