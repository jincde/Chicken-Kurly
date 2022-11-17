function sendLinkFacebook(){
    var facebook_share_url = "https://www.facebook.com/sharer/sharer.php?u={{ request.build_absolute_uri }}";
    window.open(facebook_share_url,
                'Share on Facebook',
                'scrollbars=no, width=500, height=500');
}    

function sendLinkNaver(){
    var raw_url = "{{ request.build_absolute_uri }}";
    var raw_title = "{{ }}";
    var naver_root_url = "http://share.naver.com/web/shareView.nhn?url="
    var naver_share_url = naver_root_url+encodeURI(raw_url)+"&title="+encodeURI(raw_title);
    window.open(naver_share_url,
                'Share on Naver',
                'scrollbars=no, width=500, height=500');    
}
