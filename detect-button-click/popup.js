var i = 1;
while (i <= 1) {
  chrome.tabs.create({'url': chrome.extension.getURL('popup.html')}, function(tab) {
    i = i + 1.0;
  });
}
chrome.runtime.sendMessage({directive: "popup-click"}, function(response) {
  this.close(); // close the popup when the background finishes processing request
});
// chrome.browserAction.onClicked.addListener(function(activeTab)
// {
//     var newURL = "http://www.youtube.com/watch?v=oHg5SJYRHA0";
//     chrome.tabs.create({ url: newURL });
// });

// chrome.browserAction.onClicked.addListener(function(tab) {
//     chrome.tabs.create({'url': chrome.extension.getURL('popup.html'), 'selected': true});
// });
