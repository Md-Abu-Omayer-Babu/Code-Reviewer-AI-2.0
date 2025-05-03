import React from 'react';

function Box({ color, name, style }) {
  return (
    <div
      style={style}
      className={`h-32 w-32 ${color} flex items-center justify-center text-white rounded-md`}
    >
      {name}
    </div>
  );
}

export default Box;
