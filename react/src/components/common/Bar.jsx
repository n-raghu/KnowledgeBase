import React, { useEffect, useState } from "react";
import Tabs from "./TabLinks";

function Bar() {

  const [params, setParams] = useState({
    search_key: "all",
    search_value: "",
  });

  const handleChange = (eve) => {
    setParams({
      ...params,
      search_value: eve.target.value,
    });
  };

  const handleCollection = (eve) => {
    setParams({
      ...params,
      search_key: eve.target.value,
    });
  };

  useEffect(() => {
    console.log(params);
  },[params]);

  const options = [
    {
      label: "All",
      value: "all",

    },
    {
      label: "Account",
      value: "account",
    },
    {
      label: "Opportunity",
      value: "opp",
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
            </div>
          </div>
        <Tabs />
      </nav>
    </div>

  );
}

export default Bar;
