module Lib
    ( someFunc
    ) where

someFunc :: IO ()
someFunc = putStrLn "someFunc"

-- Folds
mfoldr :: Foldable t => (a -> b -> b) -> b -> t a -> b
mfoldr f z [] = z
mfoldr f z (x:xs) = f x (mfoldr f z xs)

mfoldl :: Foldable t => (b -> a -> b) -> b -> t a -> b
mfoldl f z [] = z
mfoldl f z (x:xs) = mfoldl f (f z x) xs

minsert :: Ord a => a -> [a] -> [a]
minsert x [] = [x]
minsert x (y:ys)
  = case compare x y of
      GT -> y : minsert x ys
      _  -> x : ys

-- Insertion sort as a right fold
-- Use an insert fn and an empty list as the zero val.
minsertionSort :: Ord a => [a] -> [a]
minsertionSort = mfoldr minsert []

mlength' [] = 0
mlength' (x:xs) = 1 + mlength' xs

-- Length is a right fold.
mlength = foldr (\_ y -> y + 1) 0

