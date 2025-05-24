"use client";

import React, { useEffect, useState, useMemo, useCallback } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import ReactFlow, {
  MiniMap,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  addEdge,
} from "reactflow";
import "reactflow/dist/style.css";  // make sure reactflow styles are imported
import Navbar from "../../../components/Navbar";

function ExploreClasses() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const selectedFile = searchParams.get("file");

  const [isAllClassesClicked, setIsAllClassesClicked] = useState(false);
  const [classes, setClasses] = useState({});

  // React Flow state
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/unauthorized");
    }
  }, [router]);

  // Fetch classes and build nodes + edges
  const showAllClasses = async (fileName) => {
    try {
      const response = await fetch(
        `http://localhost:8000/class_finding/get_classes/${fileName}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      const data = await response.json();
      setClasses(data.classes || {});

      // Build React Flow nodes and edges
      buildGraph(data.classes || {});
    } catch (error) {
      console.error(error);
    }
  };

  // Build nodes and edges from class hierarchy
  const buildGraph = (classesObj) => {
    const allClasses = Object.keys(classesObj);
    const childrenSet = new Set(Object.values(classesObj).flat());

    // Find root classes (no parent)
    const rootClasses = allClasses.filter((cls) => !childrenSet.has(cls));

    // Positioning strategy (simple grid for demo)
    const nodeSpacingX = 180;
    const nodeSpacingY = 100;

    let newNodes = [];
    let newEdges = [];
    let levelMap = {}; // To track depth level of each node

    // BFS-like traversal to assign levels and create nodes/edges
    const queue = [];

    rootClasses.forEach((root, i) => {
      queue.push({ name: root, level: 0, x: i * nodeSpacingX });
      levelMap[root] = 0;
    });

    while (queue.length) {
      const { name, level, x } = queue.shift();
      const y = level * nodeSpacingY;

      newNodes.push({
        id: name,
        data: { label: name },
        position: { x, y },
        style: {
          padding: 10,
          borderRadius: 5,
          backgroundColor: "#3b82f6",
          color: "white",
          fontWeight: "bold",
          textAlign: "center",
          width: 130,
        },
      });

      if (classesObj[name] && classesObj[name].length > 0) {
        classesObj[name].forEach((child, idx) => {
          newEdges.push({
            id: `edge-${name}-${child}`,
            source: name,
            target: child,
            animated: true,
            style: { stroke: "#2563eb" },
            markerEnd: { type: "arrowclosed", color: "#2563eb" },
          });

          if (levelMap[child] === undefined) {
            levelMap[child] = level + 1;
            queue.push({ name: child, level: level + 1, x: x + idx * nodeSpacingX });
          }
        });
      }
    }

    setNodes(newNodes);
    setEdges(newEdges);
  };

  const onConnect = useCallback(
    (params) => setEdges((eds) => addEdge(params, eds)),
    [setEdges]
  );

  return (
    <div>
      <Navbar />
      <div className="flex flex-col items-center justify-center min-h-screen bg-amber-200 py-10">
        {!isAllClassesClicked && (
          <button
            className="bg-blue-500 text-white px-6 py-2 rounded mb-10"
            onClick={() => {
              setIsAllClassesClicked(true);
              showAllClasses(selectedFile);
            }}
          >
            Show All Classes
          </button>
        )}

        {isAllClassesClicked && (
          <div className="w-full h-[600px] border rounded shadow">
            <ReactFlow
              nodes={nodes}
              edges={edges}
              onNodesChange={onNodesChange}
              onEdgesChange={onEdgesChange}
              onConnect={onConnect}
              fitView
              attributionPosition="top-right"
            >
              <Controls />
              <MiniMap />
              <Background variant="dots" gap={12} size={1} />
            </ReactFlow>
          </div>
        )}
      </div>
    </div>
  );
}

export default ExploreClasses;
