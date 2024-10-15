// Can't seem to find a good way to share enums across different files in vanilla JavaScript.
// The extension is probably only a couple of JS files large anyway.
// https://stackoverflow.com/questions/44447847/enums-in-javascript-with-es6
// https://www.geeksforgeeks.org/enums-in-javascript/
const ENUMS = Object.freeze({
  NEW_POST: Symbol('NewRedditPostLoaded')
});

chrome.tabs.onUpdated.addListener((tabId, tab) => {
  if (tab.url && (
      tab.url.includes('reddit.com/r/respectthreads/comments/')
    )) {
    // https://developer.chrome.com/docs/extensions/reference/api/tabs#method-sendMessage
    chrome.tabs.sendMessage(tabId, ENUMS.NEW_POST);
  }
});
