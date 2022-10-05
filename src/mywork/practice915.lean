theorem and_commutes:
∀ (P Q : Prop), P ∧ Q → Q ∧ P   :=
begin
    assume P Q, 
    assume h: P ∧ Q, 
    let p : P := and.elim_left h,
    let q : Q := and.elim_right h, 
    apply and.intro q p, 
end
theorem or_commutes:
∀ (P Q : Prop), P ∧ Q → Q ∨ P :=
begin  
    intros P Q,
    assume h, 
    cases h with p q, 
    exact or.inr p, 
    

end
theorem baz : 
  ∀ (P Q R S: Prop),
    R → P ∨ Q ∨ R ∨ S :=
begin
    intros P Q R S,
    assume r, 
    apply or.intro_right,
    apply or.intro_right,
    apply or.intro_left,
    apply r,
end
theorem bif : ∀ (P Q R S: Prop),
    Q → R → P ∨ Q ∨ R ∨ S := 
begin
    intros P Q R S,
    assume h, 
    assume r,
    apply or.intro_right,
    apply or.intro_right,
    apply  or.intro_left,
    assumption, 
end
theorem foo : 
  ∀ (P Q R: Prop), 
    (P ∨ Q) ∧ R →
    (P ∧ R) ∨ (Q ∧ R) :=
begin
    assume P Q R h,
    cases h with pq r, 
    cases pq with p q, 

    apply or.intro_left,
    apply and.intro, 
    assumption, 
    
    assumption,

    apply or.intro_right, 
    apply and.intro,
    assumption, 

    assumption, 

end
theorem bar : 
  ∀ (P Q R S: Prop), 
    (P ∨ Q) ∧ (R ∨ S) →
    (P ∧ R) ∨ (P ∧ S) ∨ (Q ∧ R) ∨ (Q ∧ S) :=
begin
    intros P Q R S h, 
    cases h with pq rs, 
    cases pq with p q, 
    cases rs with r s, 
    
    apply or.intro_left, 
    apply and.intro p r, 

    apply or.intro_right, 
    apply or.intro_left, 
    apply and.intro p s, 

    cases rs with r s,
    apply or.intro_right,
    apply or.intro_right,
    apply or.intro_left,
    apply and.intro q r, 
    
    apply or.intro_right,
    apply or.intro_right,
    apply or.intro_right,
    apply and.intro q s, 




end