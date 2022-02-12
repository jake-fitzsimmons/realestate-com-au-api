QUERY = """
query searchByQuery($query:SearchQueryJson!$recentHides:[ListingId!]){rentSearch(query:$query recentHides:$recentHides){...RentResultsMetaData resolvedQuery{...SearchMetadata ...ResultsHeading ...SeoFooterLinks ...SearchResultsBreadcrumb __typename}marketInsights{...ResultsMarketInsightsData __typename}exclusiveShowcase{...RentExclusiveShowcaseData __typename}results{...ResultsSummary ...ResultsPagination ...RentResultsSet ...SearchResultsTotalCount exact{totalCount items{listing{...on RentResidentialListing{id productDepth __typename}...PropertyCard ...RentDetailsAboveTheFold __typename}__typename}__typename}surrounding{items{listing{...on RentResidentialListing{id productDepth __typename}...PropertyCard ...RentDetailsAboveTheFold __typename}__typename}__typename}trackingData totalResultsCount __typename}consumerContext{loggedInStatus __typename}__typename}}fragment RentResultsMetaData on RentResolvedSearch{resolvedQuery{localities{display __typename}__typename}results{__typename totalResultsCount pagination{moreResultsAvailable __typename}exact{items{listing{__typename ...on RentResidentialListing{inspections{startTime endTime __typename}_links{canonical{href __typename}__typename}__typename}...ResidentialListingAddressMetaData}__typename}__typename}}__typename}fragment ResidentialListingAddressMetaData on ResidentialListing{address{display{shortAddress fullAddress __typename}suburb state postcode __typename}__typename}fragment SearchMetadata on ResolvedQuery{metadata{canonicalSearchId savedSearchQuery __typename}__typename}fragment ResultsHeading on ResolvedQuery{localities{display __typename}__typename}fragment SeoFooterLinks on ResolvedQuery{localities{display atlasId urlValue precision name __typename}__typename}fragment SearchResultsBreadcrumb on ResolvedQuery{localities{atlasId display name urlValue precision state parents{display name urlValue precision __typename}__typename}__typename}fragment ResultsMarketInsightsData on MarketInsights{title suburbProfileUrl{href __typename}__typename}fragment RentExclusiveShowcaseData on ExclusiveShowcase{...CommonExclusiveShowcaseData listings{...on RentResidentialListing{inspections{display{shortLabel __typename}__typename}__typename}__typename}__typename}fragment CommonExclusiveShowcaseData on ExclusiveShowcase{listings{title id listingCompany{id name media{logo{templatedUrl __typename}__typename}branding{primaryColour textColour __typename}__typename}media{mainImage{templatedUrl __typename}images{templatedUrl __typename}__typename}address{suburb display{shortAddress __typename}__typename}listers{name photo{templatedUrl __typename}__typename}_links{trackedCanonical{path __typename}__typename}...PrimaryFeatures __typename}__typename}fragment PrimaryFeatures on ResidentialListing{...GeneralFeatures ...PropertySize __typename}fragment GeneralFeatures on ResidentialListing{generalFeatures{bedrooms{value __typename}bathrooms{value __typename}parkingSpaces{value __typename}__typename}__typename}fragment PropertySize on ResidentialListing{propertySizes{building{displayValue sizeUnit{displayValue __typename}__typename}land{displayValue sizeUnit{displayValue __typename}__typename}preferred{sizeType size{displayValue sizeUnit{displayValue __typename}__typename}__typename}__typename}__typename}fragment ResultsSummary on SearchResults{totalResultsCount pagination{page pageSize __typename}__typename}fragment ResultsPagination on SearchResults{pagination{maxPageNumberAvailable __typename}__typename}fragment RentResultsSet on RentSearchResults{exact{items{listing{__typename}__typename}__typename}surrounding{totalCount items{listing{__typename}__typename}__typename}pagination{page __typename}__typename}fragment SearchResultsTotalCount on SearchResults{totalResultsCount __typename}fragment PropertyCard on Listing{__typename ...ResidentialPropertyCard ...ProjectProfile}fragment ResidentialPropertyCard on ResidentialListing{...PropertyCardLayout ...BrandingOnSearchResultsConfig ...BrandingResidential badge{...Badge __typename}...ResidentialListingCardHero ...Price ...ResidentialListingCardAddress ...PropertyCardPropertyType ...PropertyCardDetailsLink ...PropertyCardAgentInfo ...ResidentialLaunchButtons ...ResidentialMediaViewerForResults ...ResidentialListingBookmark ...PrimaryFeatures ...PropertySize ...ResidentialListingCardInspection ...InspectionAuction ...DateSold ...ResidentialListingMoreButton ...ResidentialShareListing __typename}fragment PropertyCardLayout on ResidentialListing{productDepth __typename}fragment BrandingOnSearchResultsConfig on ResidentialListing{viewConfiguration{searchResults{agencyBranding __typename}__typename}productDepth __typename}fragment BrandingResidential on ResidentialListing{listingCompany{...Branding __typename}__typename}fragment Branding on ListingCompany{id name branding{primaryColour __typename}media{logo{templatedUrl __typename}__typename}__typename}fragment Badge on ListingBadge{colour label __typename}fragment ResidentialListingCardHero on ResidentialListing{...PowerProfileSlide productDepth address{display{fullAddress __typename}__typename}media{mainImage{templatedUrl __typename}images{templatedUrl __typename}floorplans{templatedUrl __typename}__typename}__typename}fragment PowerProfileSlide on ResidentialListing{media{mainImage{templatedUrl __typename}__typename}_links{canonical{path __typename}__typename}listingCompany{name media{logo{templatedUrl __typename}__typename}branding{primaryColour __typename}_links{canonical{href __typename}__typename}__typename}listers{id agentId name jobTitle photo{templatedUrl __typename}_links{canonical{href __typename}__typename}showInMediaViewer __typename}__typename}fragment Price on ResidentialListing{price{display __typename}__typename}fragment ResidentialListingCardAddress on ResidentialListing{address{suburb display{shortAddress __typename}__typename}__typename}fragment PropertyCardPropertyType on ResidentialListing{propertyType{display __typename}__typename}fragment PropertyCardDetailsLink on ResidentialListing{_links{canonical{path __typename}__typename}__typename}fragment PropertyCardAgentInfo on ResidentialListing{viewConfiguration{searchResults{agentPhoto agentName __typename}__typename}listers{name photo{templatedUrl __typename}__typename}listingCompany{branding{textColour __typename}__typename}__typename}fragment ResidentialLaunchButtons on ResidentialListing{media{threeDimensionalTours{href __typename}videos{...on YouTubeVideo{id __typename}...on ExternalVideo{href __typename}__typename}__typename}__typename}fragment ResidentialMediaViewerForResults on ResidentialListing{...ResultsAdConfiguration ...ResidentialSlides __typename}fragment ResultsAdConfiguration on ResidentialListing{viewConfiguration{searchResults{adverts{photoGallery __typename}__typename}__typename}__typename}fragment ResidentialSlides on ResidentialListing{...PowerProfileSlide ...MediaViewerEventTracking ...ThreeDimensionalTourSlide ...VideoSlide ...PhotoOverlayWithGallerySlide media{images{templatedUrl __typename}floorplans{templatedUrl __typename}__typename}__typename}fragment MediaViewerEventTracking on ResidentialListing{listers{id agentId __typename}__typename}fragment ThreeDimensionalTourSlide on ResidentialListing{media{threeDimensionalTours{href __typename}__typename}__typename}fragment VideoSlide on ResidentialListing{media{videos{...on YouTubeVideo{__typename id}__typename}__typename}__typename}fragment PhotoOverlayWithGallerySlide on ResidentialListing{...BuilderProfile ...ParentAndSiblings __typename}fragment BuilderProfile on ResidentialListing{media{mainImage{templatedUrl __typename}__typename}listingCompany{...on Builder{name _links{canonical{templated href __typename}__typename}homeDesigns{totalCount designs{name price houseSizeRange{min{displayValue value __typename}max{displayValue value __typename}__typename}generalFeaturesDisplay{bedrooms bathrooms parkingSpaces __typename}_links{canonical{href templated __typename}__typename}media{mainImage{templatedUrl __typename}__typename}__typename}__typename}__typename}__typename}__typename}fragment ParentAndSiblings on BuyResidentialListing{id media{mainImage{templatedUrl __typename}__typename}parent{name _links{canonical{path __typename}__typename}childListings{totalCount results{id media{mainImage{templatedUrl __typename}__typename}title price{display __typename}propertyType{display __typename}_links{canonical{path __typename}__typename}propertySizes{land{displayValue sizeUnit{id displayValue __typename}__typename}__typename}...PrimaryFeatures __typename}__typename}__typename}__typename}fragment ResidentialListingBookmark on ResidentialListing{id __typename}fragment ResidentialListingCardInspection on ResidentialListing{...on BuyResidentialListing{inspections{display{shortLabel longLabel __typename}__typename}__typename}...on RentResidentialListing{inspections{display{shortLabel longLabel __typename}__typename}__typename}__typename}fragment InspectionAuction on ResidentialListing{...PropertyCardAuctionDate ...ResidentialListingCardInspection __typename}fragment PropertyCardAuctionDate on BuyResidentialListing{auction{dateTime{display{shortDate __typename}__typename}__typename}__typename}fragment DateSold on ResidentialListing{...on SoldResidentialListing{dateSold{display __typename}__typename}__typename}fragment ResidentialListingMoreButton on ResidentialListing{id __typename}fragment ResidentialShareListing on ResidentialListing{_links{canonical{href __typename}__typename}address{display{fullAddress __typename}__typename}__typename}fragment ProjectProfile on ProjectProfile{badge{...Badge __typename}...ProjectProfileCardParentListing ...ProjectProfileCardAddress ...ProjectProfileCardHero ...ProjectProfileAgency ...ProjectProfileBranding ...ProjectProfileBookmark ...PropertyCardChildListings ...ProjectLaunchButtons ...ProjectProfileNextOpenTime __typename}fragment ProjectProfileCardParentListing on ProjectProfile{name title productDepth _links{canonical{path __typename}__typename}__typename}fragment ProjectProfileCardAddress on ProjectProfile{address{suburb display{shortAddress __typename}__typename}__typename}fragment ProjectProfileCardHero on ProjectProfile{productDepth address{display{fullAddress __typename}__typename}media{mainImage{templatedUrl __typename}images{templatedUrl __typename}__typename}__typename}fragment ProjectProfileAgency on ProjectProfile{listingCompany{id name media{logo{templatedUrl __typename}__typename}__typename}viewConfiguration{searchResults{agencyBranding __typename}__typename}__typename}fragment ProjectProfileBranding on ProjectProfile{name productDepth media{logo{templatedUrl __typename}__typename}branding{primaryColour __typename}__typename}fragment ProjectProfileBookmark on ProjectProfile{id __typename}fragment PropertyCardChildListings on ProjectProfile{productDepth _links{canonical{path __typename}__typename}childListings{totalCount results{id price{display __typename}media{mainImage{templatedUrl __typename}__typename}address{display{fullAddress __typename}__typename}title _links{canonical{path __typename}__typename}...PrimaryFeatures __typename}__typename}__typename}fragment ProjectLaunchButtons on ProjectProfile{media{videos{...on YouTubeVideo{id __typename}...on ExternalVideo{href __typename}__typename}__typename}__typename}fragment ProjectProfileNextOpenTime on ProjectProfile{displayLocation{nextAvailableOpeningHours{nextAvailable{display{shortLabel longLabel __typename}__typename}__typename}__typename}__typename}fragment RentDetailsAboveTheFold on RentResidentialListing{aboveTheFoldId:id id badge{...Badge __typename}...Hero ...Price ...Address ...ResidentialShareListing ...Breadcrumb_ResidentialListing ...PrimaryFeatures ...PropertyCardPropertyType ...PropertyInfoPosterBoard ...InspectionsSummaryForRent ...Bond ...DateAvailableSummary ...BrandingOnContactAgentPanelConfig ...ResidentialContactAgentBranding ...AgentInfo ...AgencyInfo ...HeaderLeaderboard ...ListingCompanyHeaderBranding ...RentResidentialListingMetaData __typename}fragment Hero on ResidentialListing{...HeroImage ...ResidentialMediaTypeBar __typename}fragment HeroImage on ResidentialListing{address{display{fullAddress __typename}__typename}viewConfiguration{details{posterBoard __typename}__typename}media{mainImage{templatedUrl __typename}images{templatedUrl __typename}floorplans{templatedUrl __typename}threeDimensionalTours{href __typename}videos{...on YouTubeVideo{id __typename}...on ExternalVideo{href __typename}__typename}__typename}__typename}fragment ResidentialMediaTypeBar on ResidentialListing{media{images{templatedUrl __typename}floorplans{templatedUrl __typename}threeDimensionalTours{href __typename}videos{...on YouTubeVideo{id __typename}...on ExternalVideo{href __typename}__typename}__typename}__typename}fragment Address on ResidentialListing{address{suburb postcode state display{shortAddress __typename}__typename}__typename}fragment Breadcrumb_ResidentialListing on ResidentialListing{__typename id address{suburb state postcode display{shortAddress __typename}__typename}propertyType{id display __typename}_links{canonical{path __typename}__typename}}fragment PropertyInfoPosterBoard on ResidentialListing{viewConfiguration{details{posterBoard __typename}__typename}__typename}fragment InspectionsSummaryForRent on RentResidentialListing{inspections{display{longLabel __typename}__typename}__typename}fragment Bond on RentResidentialListing{bond{display __typename}__typename}fragment DateAvailableSummary on RentResidentialListing{availableDate{display __typename}__typename}fragment BrandingOnContactAgentPanelConfig on ResidentialListing{viewConfiguration{details{agencyBrandingOnSidePanel __typename}__typename}__typename}fragment ResidentialContactAgentBranding on ResidentialListing{productDepth listingCompany{name branding{primaryColour __typename}media{logo{templatedUrl __typename}__typename}_links{canonical{href __typename}__typename}__typename}__typename}fragment AgentInfo on ResidentialListing{listers{name photo{templatedUrl __typename}preferredPhoneNumber _links{canonical{href __typename}__typename}__typename}listingCompany{id businessPhone __typename}__typename}fragment AgencyInfo on ResidentialListing{viewConfiguration{details{agencyInfo __typename}__typename}listingCompany{...on Agency{name __typename address{display{fullAddress __typename}__typename}_links{canonical{href __typename}__typename}}__typename}__typename}fragment HeaderLeaderboard on ResidentialListing{viewConfiguration{details{adverts{headerLeaderboard __typename}__typename}__typename}__typename}fragment ListingCompanyHeaderBranding on ResidentialListing{viewConfiguration{details{branding{header{size __typename}__typename}__typename}__typename}listingCompany{name branding{primaryColour __typename}_links{canonical{href __typename}__typename}media{logo{templatedUrl __typename}__typename}__typename}__typename}fragment RentResidentialListingMetaData on RentResidentialListing{...ResidentialListingMetaData inspections{startTime endTime __typename}__typename}fragment ResidentialListingMetaData on ResidentialListing{__typename id description media{mainImage{templatedUrl __typename}images{__typename}__typename}_links{canonical{href path __typename}__typename}propertyType{id display __typename}address{display{shortAddress fullAddress __typename}suburb state postcode __typename}price{display __typename}generalFeatures{bedrooms{value __typename}__typename}propertySizes{land{displayValue sizeUnit{displayValue __typename}__typename}__typename}}
"""
