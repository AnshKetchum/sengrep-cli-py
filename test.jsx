import React, { useState } from "react";

const Form = () => {
  const [name, setName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    console.log(`Form submitted, ${name}`);
  };

  return (
    <form className="ui form" onSubmit={this.handleSubmit}>
      <input
        type="text"
        defaultValue={this.props.element}
        onChange={this.handleChange1}
      />
      <input type="button" value="Update" className="ui positive icon button" />
    </form>
  );
};

export default Form;
