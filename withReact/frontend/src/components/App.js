import React from "react";
import ReactDOM from "react-dom";
const App = () => {
  return (
    <div>
      <p>React here!</p>
      <p>Look! This is React App!</p>
    </div>
  );
};
export default App;
ReactDOM.render(<App />, document.getElementById("app"));