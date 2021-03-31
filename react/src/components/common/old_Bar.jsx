import React, { useState } from "react";
import Tabs from "./TabLinks";

function Bar() {

  const [params, setParams] = useState()
  const handleChange = (eve) => {
    setParams['value'] = eve.target.value
    console.log("Searching for " + eve.target.value)
  };

  const handleCollection = (eve) => {
    setParams['key'] = eve.target.value
    console.log("collection " + eve.target.value)
  }

  const options = [
    {
      label: "Apple",
      value: "apple",

    },
    {
      label: "Mango",
      value: "mango",
    },
    {
      label: "Cherry",
      value: "cherry",
    }
  ]

  return (
    <div className="navbar navbar-dark bg-dark">
      <nav>
        <h1 className="text-warning">Account Lookup Service</h1>
          <div class="input-group">
            <input type="text" className="form-control" aria-label="Text input with segmented dropdown button" onChange={handleChange}></input>
            <div class="input-group-append">
              <select className="btn btn-outline-warning" onChange={handleCollection}>
                {options.map((option) => (
                  <option value={option.value}>{option.label}</option>
                ))}
              </select>
              {/* <button type="button" className="btn btn-outline-warning dropdown-toggle dropdown-toggle-split"  data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <span class="sr-only">Toggle Dropdown</span>
              </button>
              <div class="dropdown-menu">
                <a class="dropdown-item" href="#">Accounts</a>
                <a class="dropdown-item" href="#">Opportunities</a>
                <a class="dropdown-item" href="#">Organizations</a>
  </div> */}
            </div>
          </div>
        <Tabs />
      </nav>
    </div>

  );
}

export default Bar;
