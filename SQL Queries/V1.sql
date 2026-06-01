-- Evaluate proofs and generate feedback for AI as a judge evaluation and make data RAG ready.
START TRANSACTION;
-- handle re-run errors
SET SESSION autocommit = 0;

-- view data
select *
FROM proofbyindrag.v1;

-- Begin by creating all necessary columns
ALTER TABLE proofbyindrag.v1 
	ADD COLUMN total_score INT,
    ADD COLUMN quality_score VARCHAR(20),
    ADD COLUMN weaknesses LONGTEXT,
    ADD COLUMN strengths LONGTEXT,
    ADD COLUMN question LONGTEXT;

UPDATE proofbyindrag.v1
    SET question =
    'For every natural number n,
0 + 1 + 2 + ... + n = n(n + 1) / 2.'
;

UPDATE proofbyindrag.v1
SET Total_score = 
	`Identify.Base.Case` + 
	`Prove.Base.Case` + 
	`Hypothesis.is.stated` + 
	`Hypothesis.is.given.some.bound` +
    `Goal.is.Clear` +
    `Expression.of.Size.k.1.is.decomposed.into.expression.of.size.k` +
    `Inductive.Hypothesis.is.applied`;
    
UPDATE proofbyindrag.v1
    SET Quality_score = 
        CASE 
            WHEN Total_score <= 5 THEN 'Very Poor'
            WHEN Total_score <= 9 THEN 'Poor'
            WHEN Total_score <= 11 THEN 'OK'
            WHEN Total_score <= 14 THEN 'Excellent'
        END
;

UPDATE proofbyindrag.v1
SET Weaknesses = CONCAT(
    CASE `Identify.Base.Case`
        WHEN 0 THEN 'Failure to identify the base case. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Prove.Base.Case`
        WHEN 0 THEN 'Base case is not proven. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Hypothesis.is.stated`
        WHEN 0 THEN 'Failure to state the inductive hypothesis. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Hypothesis.is.given.some.bound`
        WHEN 0 THEN 'The bounds of the hypothesis are not stated. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Goal.is.Clear`
        WHEN 0 THEN 'The goal is not implicitly or explicitly stated. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Expression.of.Size.k.1.is.decomposed.into.expression.of.size.k`
        WHEN 0 THEN 'The expression at k + 1 is not decomposed into the expression of size k. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END,
    CASE `Inductive.Hypothesis.is.applied`
        WHEN 0 THEN 'Inductive hypothesis is not applied at all. '
        WHEN 1 THEN 'Partially correct but unclear or incomplete. '
        ELSE ''
    END
);

UPDATE proofbyindrag.v1
	SET Strengths = CONCAT(
    CASE WHEN `Identify.Base.Case` = 2 THEN 'Successful identification of the base case. ' ELSE '' END,
    CASE WHEN `Prove.Base.Case` = 2 THEN 'Successfully proven base case. ' ELSE '' END,
    CASE WHEN `Hypothesis.is.stated` = 2 THEN 'Inductive hypothesis is explicitly or implicitly stated. ' ELSE '' END,
    CASE WHEN `Hypothesis.is.given.some.bound` = 2 THEN 'Successfully assigns correct bounds to the hypothesis. ' ELSE '' END,
    CASE WHEN `Goal.is.Clear` = 2 THEN 'Goal is implicitly or explicitly stated. ' ELSE '' END,
    CASE WHEN `Expression.of.Size.k.1.is.decomposed.into.expression.of.size.k` = 2 
         THEN 'Successfully decomposes the expression at k + 1 into the expression at k. ' ELSE '' END,
    CASE WHEN `Inductive.Hypothesis.is.applied` = 2 
         THEN 'Successful application of the inductive hypothesis. ' ELSE '' END
);

ALTER TABLE proofbyindrag.V1
	RENAME COLUMN weaknesses TO Weaknesses,
	RENAME COLUMN strengths TO Strengths,
	RENAME COLUMN total_score to Total_score,
	RENAME COLUMN quality_score TO Quality_score,
	RENAME COLUMN question TO Question;

SELECT * 
FROM proofbyindrag.v1;

COMMIT;