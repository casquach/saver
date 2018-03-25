document.addEventListener('DOMContentLoaded', function () {
document.getElementById("connect-button").addEventListener('click',
clickHandler); });

function clickHandler(e) {   PopupClick('SHOW'); }

function PopupClick(str) {
  chrome.tabs.update({'url': "extension/html/connect.html"});
}
