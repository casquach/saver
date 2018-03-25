// chrome.runtime.onInstalled.addListener(function() {
//     chrome.storage.sync.set({color: '#3aa757'}, function() {
//       console.log('The color is green.');
//     });
//     chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
//       chrome.declarativeContent.onPageChanged.addRules([{
//         conditions: [new chrome.declarativeContent.PageStateMatcher({
//           pageUrl: {hostEquals: 'developer.chrome.com'},
//         })
//         ],
//             actions: [new chrome.declarativeContent.ShowPageAction()]
//       }]);
//     });
//   });

function doNotification () {
    var myNotification = new Notify('Yo dawg!', {
        body: 'This is an awesome notification',
        tag: 'My unique id',
        notifyShow: onShowNotification,
        notifyClose: onCloseNotification,
        notifyClick: onClickNotification,
        notifyError: onErrorNotification,
        timeout: 4
    });

    myNotification.show();
}

if (!Notify.needsPermission) {
    doNotification();
} else if (Notify.isSupported()) {
    Notify.requestPermission(onPermissionGranted, onPermissionDenied);
}

function onPermissionGranted() {
	console.log('Permission has been granted by the user');
	doNotification();
}

function onPermissionDenied() {
	console.warn('Permission has been denied by the user');
}

function onNotifyShow() {
	console.log('notification was shown!');
}
