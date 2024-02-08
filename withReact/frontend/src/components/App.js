import React from "react";
import ReactDOM from "react-dom";
const App = () => {
  return (
    <div>
      <p>React here!</p>
      <p>Look! This is React App!</p>
      <h1>Hello World</h1>
    </div>
  );
};
export default App;
ReactDOM.render(<App />, document.getElementById("app"));