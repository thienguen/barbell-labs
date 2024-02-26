import { Dispatch, SetStateAction } from "react";
import { SettingsInterface } from "../context/AlgorithContext.types";

export function generateArray(arrayLen: number) {
  return Array.from(
    { length: arrayLen },
    () => Math.floor(Math.random() * 60) + 20
  );
}

export function bubbleSort(inputArr: number[]) {
  const bubbleArr = [...inputArr];
  const bubbleAnim: number[][] = [];
  const len = bubbleArr.length;
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (bubbleArr[j] > bubbleArr[j + 1]) {
        bubbleAnim.push([j + 1, j]);
        const tmp = bubbleArr[j];
        bubbleArr[j] = bubbleArr[j + 1];
        bubbleArr[j + 1] = tmp;
      }
    }
  }
  return { bubbleArr, bubbleAnim };
}

export function insertionSort(inputArr: number[]) {
  const insertionArr = [...inputArr];
  const insertionAnim: number[][] = [];
  const length = insertionArr.length;
  for (let i = 1; i < length; i++) {
    let j = i;
    while (j > 0 && insertionArr[j - 1] > insertionArr[j]) {
      insertionAnim.push([j - 1, j]);
      const tmp = insertionArr[j - 1];
      insertionArr[j - 1] = insertionArr[j];
      insertionArr[j] = tmp;
      j--;
    }
  }

  return { insertionArr, insertionAnim };
}

function updateBackgroundColor(element, color) {
  element.style.backgroundColor = color;
}

function swapHeights(element1, element2) {
  const tempHeight = element1.style.height;
  element1.style.height = element2.style.height;
  element2.style.height = tempHeight;
}

function resetBackgroundColor(element) {
  element.style.backgroundColor = "originalBg";
}

function handleFinalState(setArray, sortArr, idx, length) {
  if (idx === length - 1) setArray(sortArr);
}

async function animateSort(animArr, sortArr, settings, setArray) {
  const originalBg = "rgb(79 70 229)";

  for (let idx = 0; idx < animArr.length; idx++) {
    const [start, end] = animArr[idx];
    const startDiv = document.getElementById(`${start}`);
    const endDiv = document.getElementById(`${end}`);

    if (!startDiv || !endDiv) continue;

    updateBackgroundColor(startDiv, "rgb(239 68 68)");
    updateBackgroundColor(endDiv, "rgb(239 68 68)");

    swapHeights(startDiv, endDiv);

    await new Promise<void>((resolve) =>
      setTimeout(() => {
        updateBackgroundColor(startDiv, originalBg);
        updateBackgroundColor(endDiv, originalBg);
        resolve();
      }, settings.sortingSpeed * 2)
    );

    handleFinalState(setArray, sortArr, idx, animArr.length);
  }
}
