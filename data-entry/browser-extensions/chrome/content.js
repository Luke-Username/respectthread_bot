const ENUMS = Object.freeze({
  NEW_POST: Symbol('NewRedditPostLoaded')
});

// For elements that take longer to load, try to get it n times, waiting 1 second between each try. Return once it has it.
const getContainer = async (query) => {
  const attempts = 20;

  for (let i = 0; i < attempts; i++) {
    console.log(`Query ${i}`)
    const container = document.querySelector(query);
    if (container) return container;
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  return null;
};

const getCurrentPostData = () => {
  let postTitle = document
    .querySelector('p.title')
    .querySelector('a.title.may-blank.loggedin')
    .innerText;
  
  // Apostrophes (') are a reserved character in Postgres. Need to escape them by doubling them ('').
  if (postTitle.includes("'")) {
    postTitle = `"${postTitle.replace("'", "''")}"`;
  }
  else {
    postTitle = `'${postTitle}'`;
  }
  
  const shortLink = document.querySelector('input#shortlink-text').value;
  
  const postData = `id = get_rt_id(cur, ${postTitle}, '${shortLink}')`;
  navigator.clipboard.writeText(postData)
    .then(() => console.log('Text copied to clipboard'))
    .catch((err) => console.error('Error copying text:', err));
};

const addCopyToClipboardButton = (titleContainer) => {
  if (titleContainer == null) return;

  const clipboardButtonExists = titleContainer?.getElementsByClassName('clipboard-button')[0];
  if (clipboardButtonExists) return;

  // Add button
  const clipboardButton = document.createElement('button');
  clipboardButton.className = 'clipboard-button';
  clipboardButton.title = 'Copy post title, author, and URL to clipboard';

  // Add icon for button
  const copyIcon = document.createElement('img');
  copyIcon.className = 'clipboard-button-icon'
  copyIcon.src = chrome.runtime.getURL('clipboard-semi-transparent.svg');
  clipboardButton.appendChild(copyIcon);

  const currentUrl = window.location.href;
  if (currentUrl.includes('reddit.com/r/respectthreads/comments/')) {
    clipboardButton.addEventListener('click', getCurrentPostData);
  }

  titleContainer?.insertBefore(clipboardButton, titleContainer.firstChild);
};

const newPostLoaded = async () => {
  // Insert 'Copy to Clipboard' button for the original post
  const titleContainer =  await getContainer('p.title');
  addCopyToClipboardButton(titleContainer);
};

(() => {
  // https://developer.chrome.com/docs/extensions/reference/api/runtime#example-content-msg
  chrome.runtime.onMessage.addListener(async (message) => {
    if (message ===  ENUMS.NEW_POST) {
      newPostLoaded();
    }
  });

  // Quick fix. Helps load in the copy button without having to navigate away from the page.
  newPostLoaded();
})(); // Can't forget () at the end of this anonymous function, or you'll get an error "Receiving end does not exist" that's really hard to troubleshoot for 
