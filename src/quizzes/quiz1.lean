/-
CS2120 Fall 2022 Sullivan. Quiz #1. Edit your answers into
this file using VSCode. Save the file to your *local* hard 
drive (File > Save As > local > ...). Submit it to the Quiz1
assignment on Collab.
-/

/-
#1: For each of the following questions give a yes/no answer 
and then a very brief explanation why that answer is correct.
To explain why your answer is correct, name the specific rule
of inference that tells you it's correct, or explain that 
there is no such valid inference rule.
-/

/-
#1A

If a ball, b, is round *and* b is also red, is b red?

A: yes/no: 
Yes
B: Why? 
And elimination right. 


#1B

If flowers make you happy and chocolates make you happy,
and I give you flowers *or* I give you chocolates, will
you be happy?

A: yes/no: 
Yes
B: Why?
A combination of the And elimination and Or introduction rules.
We can first use the and elimination(left and right) to conclude that the two 
propositions (flowers makes you happy/ choclates make you happy) are both true.
Then we can use or introduction(left and right) to make show that (Flowers happy OR Choclaotes happy)
is true since both of the propositions are true.

#1C: If giraffes are just zebras in disguise, then the 
moon is made of green cheese?

A. yes/: 
Yes
B. Why?
False elimination

#1D. If x = y implies that 0 = 1, then is it true that
x ≠ y?

A. yes/no: 
Yes
B. Why?
We can either assume that x = y is false thats the only way for the first implication to be true,
and from there we can determine that x and y are not equal to each other. 
Or we can assume the first implication to be false, and use false elimination.


#1E. If every zebra has stripes and Zoe is a Zebra then
Zoe has stripes.

A. yes/no: 
Yes
B. Why?
Arrow elimination


#1F. If Z could be *any* Zebra and Z has stripes, then 
*every* Zebra has stripes.

A. Yes/no: 
No
B: Why?
We are currently applying information about specific example to a population,
but we can't do that. We don't know if other Zebras are similar to Z, so 
we cannot conclude that every zibra has stripes.

#1G. If whenever the wind blows, the leaves move, and 
the leaves are moving, then the wind is blowing.

A. yes/no: 
No
B. Why? 
There can be other things that cause the leaves to move.

#1H: If Gina is nice *or* Gina is tall, and Gina is nice,
then Gina is not tall. (The "or" here is understood to be
the or of predicate logic.)

A. yes/no: 
No
B. Why?
We cannot prove that Gina is not nice and tall since she could be that.
-/



/- 
#2

Consider the following formula/proposition in propositional
logic: X ∨ ¬Y.

#2A: Is is satisfiable? If so, give a model (a binding of 
the variables to values that makes the expressions true).
Yep, X = true, Y = False

#2B: Is it valid? Explain your answer. 
Nope, a valid proposition will always be true no matter the intrepretations. 
The intrepretation X = false and Y = true makes this propsition false so it is not valid.

-/


/-
#3: 

Express the following propositions in predicate logic, by
filling in the blank after the #check command.

If P and Q are arbitrary (any) propositions, then if (P is 
true if and only if Q is true) then if P is true then Q is 
true.
-/

#check ∀(P Q : Prop), P  ↔ Q  → P → Q



/-
#4 Translate the following expressions into English.
The #check commands are just Lean commands and can
be ignored here. 
-/


-- A
#check ∀ (n m : ℕ), n < m → m - n > 0

/-
Answer: If n and m are both natural numbers, then if m is larger than n, then 
m -n would be greater than zero.
-/

-- B

#check ∃ (n : ℕ), ∀ (m : nat), m >= n

/-
Answer:If there is some n that is a natural number, and if all m are natural numbers, then m must be larger or equal to n is true.
-/


-- C

variables (isEven: ℕ → Prop) (isOdd: ℕ → Prop)
#check ∀ (n : ℕ), isEven n ∨ isOdd n

/-
Answer: If a natural number can either be even or odd, then 
it is true that every natural number n can be even or odd. 
-/


-- D

#check ∀ (P : Prop), P ∨ ¬P

/-
Answer: For all propositions P,P or the opposite of P must be true
-/


-- E

#check ∀ (P : Prop), ¬(P ∧ ¬P)

/-
Answer: For all propositions P, the opposite of (P and the opposite of P) must be true.
-/


/-
#5 Extra Credit

Next we define contagion as a proof of a slightly long
proposition. Everything before the comma introduces new
terms, which are then used after the comma to state the
main content of the proposition. 

Using the names we've given to the variables to infer
real-world meanings, state what the logic means in plain
natural English. Please don't just give a verbatim reading
of the formal logic. 
  If animal a1 has a virus and is in close contact with animal a2, then 
  a2 also has a virus. 
-/

variable contagion : 
  ∀ (Animal : Type) 
  (hasVirus : Animal → Prop) 
  (a1 a2 : Animal) 
  (hasVirus : Animal → Prop)
  (closeContact : Animal → Animal → Prop), 
  hasVirus a1 → closeContact a1 a2 → hasVirus a2


