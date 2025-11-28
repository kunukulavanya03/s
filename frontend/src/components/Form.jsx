import React from 'react';
function Form() {
  return (
    <form className="flex flex-col space-y-4">
      <input type="text" className="p-2 border border-gray-400 rounded" placeholder="Name" />
      <input type="email" className="p-2 border border-gray-400 rounded" placeholder="Email" />
      <textarea className="p-2 border border-gray-400 rounded" placeholder="Message"></textarea>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Submit</button>
    </form>
  );
}
export default Form;