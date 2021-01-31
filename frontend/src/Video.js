import './Video.css';
import React from "react";
import YouTube from 'react-youtube-embed'

class Video extends React.Component {
 
  render (){
    function textBox(){
        var box = document.createElement("input");
        box.type="text";
      }

    /*
    const [videoFilePath, setVideoFileURL] = useState(null);
    const handleVideoUpload = (event) => {
    setVideoPath(URL.createObjectURL(event.target.files[0]));
    */

    return (
      <div className="Video">
        <YouTube className="ytvid" id='A71aqufiNtQ' />
        <header className="Video-header">
          <input type="text" className ="keysearch" placeholder="type something here..." onClick={textBox}></input>
        </header>
      </div>
    );
}
}
export default Video;