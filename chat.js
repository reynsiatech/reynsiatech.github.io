(function(d, m){
  var kommunicateSettings = {
    "appId":"3a3960457e42c8754ac7fd948544dbd7c", //"popupWidget":true,"automaticChatOpenOnNavigation":true};
    "onInit": function () {
              var iframe = parent.document.getElementById("kommunicate-widget-iframe"),
                  launcher = KommunicateGlobal.document.getElementById('mck-sidebox-launcher'),
                  preChatPopup = KommunicateGlobal.document.querySelector('#chat-popup-widget-container .chat-popup-widget-text-wrapper'),
                  closeButton = KommunicateGlobal.document.getElementById('km-chat-widget-close-button');

              closeButton.addEventListener('click', function () {
                  iframe.classList.remove("change-kommunicate-iframe-height");
                  Kommunicate.displayKommunicateWidget(false);
              });
              Kommunicate.displayKommunicateWidget(false);
          }
      };
      var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
      s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
      var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
      window.kommunicate = m; m._globals = kommunicateSettings;
  })(document, window.kommunicate || {});

  function openChat() {
      Kommunicate.displayKommunicateWidget(true);
      Kommunicate.launchConversation();
  }
