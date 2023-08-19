// Example: Log the URLs of all web requests
chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    console.log("URL:", details.url);
    // Check if the URL is from YouTube and track the watchtime
  },
  {urls: ["<all_urls>"]}, // Filter to monitor all web requests
  ["blocking"] // Use the "blocking" permission to intercept requests
);