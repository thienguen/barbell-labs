import React from 'react';

interface WidgetProps {
  title: string;
  data: number[];
}

const DashboardWidget: React.FC<WidgetProps> = ({ title, data }) => {
  const renderDataPoints = () => {
    return data.map((point, index) => (
      <div key={index} className="p-2 bg-gray-200 rounded shadow-sm">
        <p className="text-sm text-gray-700">{`Point ${index + 1}: ${point}`}</p>
      </div>
    ));
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow-md">
      <h2 className="mb-4 text-lg font-semibold text-gray-800">{title}</h2>
      <div className="grid grid-cols-3 gap-4">
        {renderDataPoints()}
      </div>
    </div>
  );
};

export default DashboardWidget;
