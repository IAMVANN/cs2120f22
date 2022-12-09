import data.set

/-
- existence propositions and proofs
  -- introduction rule
  -- elimination rule
  -- proofs involving existence

- set theory
  -- membership predicates
  -- set operations and notations
    - membership, ∈ 
    - intersection, ∩ 
    - union, ∪ 
    - complement, ᶜ 
    - difference, \
    - subset relation, ⊆, ⊂ 
    - powerset 𝒫 (the set of all subsets of a given set)
  -- propositions and proofs

  - relations
  -- membership predicates (on pairs of values)
  -- domain, domain of definition, co-domain, range
  -- properties of relations
  -- total is when every element in the domain is in the domain of definition
  --Surjective - the range is the entire codomain; the codomain version of total
    - single-valuedness (functionality)
    - reflexivity
    - symmetry
    - transitivity
    - equivalence
    - asymmetry
    - anti-symmetry
  -- properties of functions
    - surjectivity - 
    - injectivity - one to one
    - bijectivity - 
    what does it mean to mean single valued
    - cannot have an element in a domain have 2 outputs
    - a domain can only have 1 ouptut; (doesn't mean 2 domains can't have the same output)
  - induction
    -- inductive data definitions
    -- induction axioms (for enumerated types and ℕ)
    -- definition of recursive functions
    -- construction of proofs by induction
-/

/-
I asked ChatGPT whether 0 = 1 implies 2 = 3. Here's 
the answer I got. So just how smart is ChatGPT?

"No, 0 does not equal 1 and therefore the statement 
"0 = 1 implies that 2 = 3" is not true. In mathematics, 
the equal sign (=) is used to indicate that two 
expressions are equal in value. So, if 0 did equal 1, 
then it would be true that 2 equals 3 because any 
number multiplied by 0 is equal to 0. But since 0 
does not equal 1, the statement is not true." 
  -/