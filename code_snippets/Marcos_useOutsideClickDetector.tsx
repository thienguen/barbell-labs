import { type RefObject, useEffect } from "react";

/**
 * Custom hook to detect clicks outside a specified element.
 * @param ref - Reference to the HTML element for which outside clicks should be detected.
 * @param callback - Callback function to be executed when an outside click is detected.
 */
const useOutsideClickDetector = (
  ref: RefObject<HTMLDivElement>,
  callback: () => void
) => {
  useEffect(() => {
    /**
     * Event handler to check if a click occurred outside the specified element.
     * @param e - MouseEvent object representing the click event.
     */
    const handleClickOutside = (e: MouseEvent) => {
      // Check if the specified element exists and if the click occurred outside it
      if (ref.current && !ref.current.contains(e.target as Node)) {
        // Execute the provided callback when an outside click is detected
        callback();
      }
    };

    // Add mousedown event listener to the entire document
    document.addEventListener("mousedown", handleClickOutside);

    // Cleanup function to remove the event listener when the component unmounts or dependencies change
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [ref, callback]); // Re-run the effect when the ref or callback function changes
};

export default useOutsideClickDetector;
