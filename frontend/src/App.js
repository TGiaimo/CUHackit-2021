import './App.css';
import React from "react";
//import { withRouter } from 'react-router-dom'

class App extends React.Component {
  /*
  constructor(props){
    super(props);
    this

    textBox(){
        var box = document.createElement("input");
        box.type="text";
      }

    }
  }

  import { Route } from 'react-router-dom'

const Button = () => (
  <Route render={({ history}) => (
    <button
      type='button'
      onClick={() => { history.push('/new-location') }}
    >
      Click Me!
    </button>
  )} />
)
  */
 
  render (){
    function textBox(){
        var box = document.createElement("input");
        box.type="text";
        //this.props.history.push('/Video');
      }
    return (
      <div className="App">
        <header className="App-header">
          <p className="Ent-keyp1">
            Enter keyword:
          </p>
          <input type="text" className ="keysearch" placeholder="type something here..." onClick={textBox}></input>
        </header>
      </div>
    );
}
}
export default App;