/**
 * Default comparator supporting numbers, strings, bigints and Dates.
 * @template T
 * @param {T} a
 * @param {T} b
 * @returns {boolean} True if a <= b
 */
const defaultIsLessOrEqual = (a, b) => a <= b;

/**
 * A stack supporting O(1) push, pop and findMin operations.
 * @template T
 */
export class MinStack {
    /**  @type {T[]} */
    #data = [];
    /**  @type {T[]} */
    #mins = [];
    /**  @type {(a: T, b: T) => boolean} */
    #isLessOrEqual;
    /**
     * @param {(a: T, b: T) => boolean} [isLessOrEqual] Optional custom comparator
     */
    constructor(isLessOrEqual = defaultIsLessOrEqual) {
        this.#isLessOrEqual = isLessOrEqual;
    }

    /**
     * Pushes an element onto the stack in O(1) time.
     * @param {T} x
     * @returns {void}
     */
    push(x) {
        this.#data.push(x);
        if (
            this.#mins.length === 0 ||
            this.#isLessOrEqual(x, this.#mins.at(-1))
        ) {
            this.#mins.push(x);
        }
    }

    /**
     * Removes and returns the top element in O(1) time.
     * @returns {T}
     * @throws {RangeError} If the stack is empty.
     */
    pop() {
        if (this.#data.length === 0) {
            throw new RangeError("pop from empty MinStack");
        }
        const val = /**  @type {T} */ (this.#data.pop());
        if (this.#isLessOrEqual(val, this.#mins.at(-1))) {
            this.#mins.pop();
        }
        return val;
    }

    /**
     * Returns the minimum element in the stack in O(1) time without removing it.
     * @returns {T}
     * @throws {RangeError} If the stack is empty.
     */
    findMin() {
        if (this.#mins.length === 0) {
            throw new RangeError("findMin from empty MinStack");
        }
        return /**  @type {T} */ (this.#mins.at(-1));
    }
}
